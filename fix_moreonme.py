import re

file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Hapus section MORE ON ME beserta CSS-nya
content = re.sub(r'\n\n    /\* MORE ON ME badges \*/.*?\.more-badge\.accent \{[^}]+\}', '', content, flags=re.DOTALL)
content = re.sub(r'\n<!-- MORE ON ME -->.*?</section>\n', '\n', content, flags=re.DOTALL)

# 2. Tambah tombol More on Me di hero-cta setelah tombol Download CV
old = '</div>\n        </div>\n\n    </div>\n\n  </div>\n\n</section>\n\n\n\n<!-- SUMMARY -->'
new = '''</div>
        </div>
        <a href="#summary" class="btn-more-on-me">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
          More on Me
        </a>

    </div>

  </div>

</section>



<!-- SUMMARY -->'''

content = content.replace(old, new)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
