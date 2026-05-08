file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Hapus tombol More on Me yang salah posisi (di dalam btn-download div)
content = re.sub(
    r'\s*<a href="#summary" class="btn-more-on-me">.*?</a>\s*',
    '\n',
    content,
    flags=re.DOTALL
)

# Tambah tombol More on Me setelah </div> penutup hero-cta, sebelum </div> hero-right
# Cari pola: penutup hero-cta lalu hero-right
old = '      </div>\n\n    </div>\n\n\n  </div>\n\n\n</section>'
new = '''      </div>
      <a href="#summary" class="btn-more-on-me">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
        More on Me
      </a>

    </div>


  </div>


</section>'''

content = content.replace(old, new)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
