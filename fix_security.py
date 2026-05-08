import re

file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Reverse Tabnabbing - tambah rel="noopener noreferrer" ke semua target="_blank"
# Case: sudah ada rel tapi tidak lengkap, atau belum ada rel sama sekali
def fix_tabnabbing(match):
    tag = match.group(0)
    if 'rel=' in tag:
        # update existing rel
        tag = re.sub(r'rel=["\'][^"\']*["\']', 'rel="noopener noreferrer"', tag)
    else:
        # tambah rel sebelum penutup >
        tag = tag.rstrip('>').rstrip('/') .rstrip() + ' rel="noopener noreferrer">'
    return tag

content = re.sub(r'<a [^>]*target=["\']_blank["\'][^>]*>', fix_tabnabbing, content)

# 2. Fix iframe - tambah sandbox attribute
content = content.replace(
    '<iframe id="certModalFrame" src="">',
    '<iframe id="certModalFrame" src="" sandbox="allow-scripts allow-same-origin allow-forms">'
)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
