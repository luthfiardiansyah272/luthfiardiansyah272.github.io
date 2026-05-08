file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Gained hands-on exposure to production digitalization' in line:
        lines[i] = line.rstrip('\n').rstrip('\r') + '\n'
        lines.insert(i+1, '        <li>Assisted in sensor installation and configuration for vehicle activity tracking systems across plantation units.</li>\n')
        lines.insert(i+2, '        <li>Supported User Acceptance Testing (UAT) and documented findings to ensure system readiness before full deployment.</li>\n')
        break

with open(file, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('done')
