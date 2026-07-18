from weasyprint import HTML

html = """
<!DOCTYPE html>
<html>
<head>
<style>
  a::after { content: target-counter(attr(href), page); }
  a.arabic::after { content: target-counter(attr(href), page, arabic-indic); }
</style>
</head>
<body>
  <div id="p1" style="break-after: page;">Page 1</div>
  <div id="p2" style="break-after: page;">Page 2</div>
  <a href="#p1">Link to p1: </a><br>
  <a class="arabic" href="#p2">Link to p2 (arabic): </a>
</body>
</html>
"""
doc = HTML(string=html).render()
for page in doc.pages:
    print(page)
