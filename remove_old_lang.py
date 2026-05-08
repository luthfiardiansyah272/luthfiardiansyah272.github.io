import re

file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Hapus function setLanguage dan semua isinya
content = re.sub(r'\n  function setLanguage\(lang\) \{.*?\n  \}', '', content, flags=re.DOTALL)

# Hapus sisa kode yang memanggil setLanguage
content = re.sub(r'\n  // Set initial language\n  if \(currentLanguage.*?\}\n', '\n', content, flags=re.DOTALL)
content = re.sub(r'\n  languageToggle\.addEventListener.*?\}\);\n', '\n', content, flags=re.DOTALL)
content = re.sub(r'\n  const languageToggle.*?;\n', '\n', content)
content = re.sub(r'\n  const currentFlag.*?;\n', '\n', content)
content = re.sub(r'\n  const currentLang.*?;\n', '\n', content)
content = re.sub(r'\n  const currentLanguage.*?;\n', '\n', content)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

# Verifikasi
with open(file, 'r', encoding='utf-8') as f:
    c = f.read()
count_setlang = c.count('function setLang(')
count_setlanguage = c.count('function setLanguage(')
print(f'setLang: {count_setlang}, setLanguage: {count_setlanguage}')
