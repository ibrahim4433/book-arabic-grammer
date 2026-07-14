import os
import glob
import json
import re
import difflib
from bs4 import BeautifulSoup

def normalize_text(text):
    if not text:
        return ""
    # Remove zero-width chars and spaces
    t = re.sub(r'[\s\u200b\u200c\u200d\u200e\u200f]', '', text)
    # Normalize alefs
    t = re.sub(r'[أإآا]', 'ا', t)
    # Remove tashkeel for better matching
    t = re.sub(r'[\u0617-\u061A\u064B-\u0652]', '', t)
    return t

def clean_title(text):
    text = text.replace('إِجَابَاتُ: ', '').strip()
    text = re.sub(r'\(الْجُزْءُ.*?\)', '', text)
    text = re.sub(r'\(الجزء.*?\)', '', text)
    text = re.sub(r'\(الدَّرْسُ.*?\)', '', text)
    text = re.sub(r'_تابع', '', text)
    text = re.sub(r'^[\d\.\s-]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def main():
    # 1. Load AI recovered answers
    recovered_list = []
    for filepath in glob.glob('chunks/answers_*.json'):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if 'answers' in data:
                recovered_list.extend(data['answers'])

    recovered_dict = {}
    for item in recovered_list:
        norm_q = normalize_text(item['question'])
        recovered_dict[norm_q] = item['answer']

    # 2. Load old answers
    old_answers_dict = {}
    old_answer_titles_map = {} # norm_title -> title
    for p in glob.glob('backup_answers/*.html'):
        with open(p, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        headers = soup.find_all('div', class_='block-header')
        bodies = soup.find_all('div', class_='block-body')
        
        for h, b in zip(headers, bodies):
            title_span = h.find('span')
            if not title_span: continue
            title_text = clean_title(title_span.get_text())
            norm_title = normalize_text(title_text)
            
            if norm_title not in old_answers_dict:
                old_answers_dict[norm_title] = []
                old_answer_titles_map[norm_title] = title_text
                
            old_answers_dict[norm_title].extend(b.find_all('li'))

    # 3. Match
    unified_final_answers = {} 
    pages = sorted(glob.glob('pages/*.html'))
    
    for page in pages:
        if '98.' in page or 'TOC' in page or '99.' in page or '00.1' in page or '00.2' in page or '00.0' in page:
            continue
            
        with open(page, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        title_tag = soup.find('title')
        if not title_tag: continue
        unified_title = clean_title(title_tag.get_text())
        norm_title = normalize_text(unified_title)
        
        if unified_title not in unified_final_answers:
            unified_final_answers[unified_title] = []
            
        exam_blocks = soup.find_all('div', class_='exam-question')
        if not exam_blocks:
            continue
            
        # Match with old_answers_dict
        matched_norm_title = None
        if norm_title in old_answers_dict:
            matched_norm_title = norm_title
        else:
            matches = difflib.get_close_matches(norm_title, old_answers_dict.keys(), n=1, cutoff=0.6)
            if matches:
                matched_norm_title = matches[0]

        for block in exam_blocks:
            q_elements = block.find_all('li')
            if not q_elements:
                p_tag = block.find('p')
                if p_tag:
                    q_elements = [p_tag]
                    
            for q_el in q_elements:
                # Remove marker or exam-number temporarily
                marker = q_el.find('span', class_=['marker', 'exam-number'])
                if marker: marker.extract()
                
                strong = q_el.find('strong')
                if strong: strong.extract()
                
                q_text = q_el.get_text().replace('السُّؤَالُ:', '').strip()
                q_norm = normalize_text(q_text)
                
                matched = False
                
                # Check AI recovered
                if q_norm in recovered_dict:
                    ans_html = recovered_dict[q_norm]
                    unified_final_answers[unified_title].append(ans_html)
                    del recovered_dict[q_norm]
                    matched = True
                else:
                    rec_norm = normalize_text(q_text)
                    for k in list(recovered_dict.keys()):
                        if rec_norm in k or k in rec_norm:
                            ans_html = recovered_dict[k]
                            unified_final_answers[unified_title].append(ans_html)
                            del recovered_dict[k]
                            matched = True
                            break
                            
                if not matched:
                    if matched_norm_title and len(old_answers_dict[matched_norm_title]) > 0:
                        old_li = old_answers_dict[matched_norm_title].pop(0)
                        
                        ans_span = old_li.find('span', class_='highlight-green')
                        if ans_span:
                            ans_content = "".join([str(c) for c in ans_span.contents])
                            ans_html = f'<span><strong>السُّؤَالُ:</strong> {q_text}<br/><span class="highlight-green">{ans_content}</span></span>'
                        else:
                            ans_html = f'<span><strong>السُّؤَالُ:</strong> {q_text}<br/><span class="highlight-green"><strong>الْجَوَابُ:</strong> إجابة غير متوفرة.</span></span>'
                            
                        unified_final_answers[unified_title].append(ans_html)
                    else:
                        ans_html = f'<span><strong>السُّؤَالُ:</strong> {q_text}<br/><span class="highlight-green"><strong>الْجَوَابُ:</strong> إجابة غير متوفرة.</span></span>'
                        unified_final_answers[unified_title].append(ans_html)

    # 4. Write output
    with open('pages/98.00_p120_Answers.html', 'r', encoding='utf-8') as f:
        out_html = f.read()
    
    soup_out = BeautifulSoup(out_html, 'html.parser')
    
    wrapper = soup_out.find('div', class_='force-new-page')
    
    # Remove old answers
    for header in wrapper.find_all('div', class_='block-header'):
        header.decompose()
    for body in wrapper.find_all('div', class_='block-body'):
        body.decompose()
        
    for title, ans_list in unified_final_answers.items():
        if not ans_list: continue
        
        header_div = soup_out.new_tag('div', attrs={'class': 'block-header accent'})
        span = soup_out.new_tag('span')
        span.string = f'إِجَابَاتُ: {title}'
        header_div.append(span)
        wrapper.append(header_div)
        
        body_div = soup_out.new_tag('div', attrs={'class': 'block-body'})
        ul = soup_out.new_tag('ul', attrs={'class': 'structured-list'})
        
        for idx, ans_html in enumerate(ans_list, 1):
            li = soup_out.new_tag('li')
            
            marker = soup_out.new_tag('span', attrs={'class': 'marker'})
            
            # Arabic-Indic digits conversion
            arabic_indic = {'0':'٠','1':'١','2':'٢','3':'٣','4':'٤','5':'٥','6':'٦','7':'٧','8':'٨','9':'٩'}
            idx_str = str(idx)
            for k,v in arabic_indic.items():
                idx_str = idx_str.replace(k, v)
                
            marker.string = idx_str
            li.append(marker)
            
            content_span = BeautifulSoup(ans_html, 'html.parser')
            li.append(content_span)
            
            ul.append(li)
            
        body_div.append(ul)
        wrapper.append(body_div)
        
    with open('pages/98.00_p120_Answers.html', 'w', encoding='utf-8') as f:
        f.write(str(soup_out))
        
    print(f"Generated unified answers for {len([k for k,v in unified_final_answers.items() if v])} titles!")

if __name__ == '__main__':
    main()
