$css = Get-Content -Raw -Path 'C:\Users\ibrah\Documents\GitHub\book-arabic-grammer\styles\main.css'
$css = $css -replace 'font-weight:\s*400;', 'font-weight: 700;'
$css = $css -replace 'font-weight:\s*500;', 'font-weight: 700;'
$css = $css -replace 'font-weight:\s*normal', 'font-weight: 700'
$css = $css -replace '--color-primary:\s*#[0-9a-fA-F]+;', '--color-primary: #1E8449;'
$css = $css -replace '--color-accent:\s*#[0-9a-fA-F]+;', '--color-accent: #D4AC0D;'
$css = $css -replace '--color-dark:\s*#[0-9a-fA-F]+;', '--color-dark: #145A32;'
$css = $css -replace '--color-light:\s*#[0-9a-fA-F]+;', '--color-light: #F9E79F;'
$css = $css -replace 'background-image:\s*url\([^)]+\);', "background-image: url('../v3.png');"
$css = $css -replace '#E0F2F1', 'var(--color-light)'
$css = $css -replace '#004D40', 'var(--color-dark)'

$dir = 'C:\Users\ibrah\Documents\GitHub\book-arabic-grammer\new-style-options\v3'
New-Item -ItemType Directory -Force -Path $dir | Out-Null
Set-Content -Path "$dir\main.css" -Value $css -Encoding utf8
