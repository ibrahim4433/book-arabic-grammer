$content = Get-Content -Path "..\..\styles\main.css" -Raw

$content = $content -replace '--color-primary:\s*#[0-9A-Fa-f]+;', '--color-primary: #34495E;'
$content = $content -replace '--color-accent:\s*#[0-9A-Fa-f]+;', '--color-accent: #F1948A;'
$content = $content -replace '--color-dark:\s*#[0-9A-Fa-f]+;', '--color-dark: #2C3E50;'
$content = $content -replace '--color-light:\s*#[0-9A-Fa-f]+;', '--color-light: #E5E7E9;'

$content = $content -replace "url\('\.\./assets/page-background/background\.png'\)", "url('../v7.png')"

$content = [regex]::Replace($content, 'font-weight:\s*(normal|bold|\d+)', {
    param($match)
    if ($match.Groups[1].Value -eq '900') {
        return 'font-weight: 900'
    } else {
        return 'font-weight: 700'
    }
})

Set-Content -Path "main.css" -Value $content -Encoding UTF8
