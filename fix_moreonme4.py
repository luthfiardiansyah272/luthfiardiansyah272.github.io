import re

file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Hapus semua btn-more-on-me yang ada
content = re.sub(r'\s*<a href="#summary" class="btn-more-on-me">.*?</a>', '', content, flags=re.DOTALL)

# Fix: ganti blok hero-cta closing + hero-right closing yang berantakan
# Cari dari </div> penutup btn-download-menu sampai </section>
old_pattern = r'(</div>\s*\n\s*</div>\s*\n\s*\n\s*</div>\s*\n\s*\n\s*</div>\s*\n\s*\n\s*</div>\s*\n\s*\n\s*</div>\s*\n\s*\n\s*</section>)'

new_block = '''          </div>
        </div>
      </div>
      <a href="#summary" class="btn-more-on-me">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
        More on Me
      </a>
    </div>
  </div>
</section>'''

# Cari posisi </section> pertama setelah hero dan rebuild
# Lebih aman: cari dari CV Palembang sampai </section>
old = re.search(r'CV &ndash; Palembang.*?</section>', content, re.DOTALL)
if old:
    replacement = '''CV &ndash; Palembang
            </a>
          </div>
        </div>
      </div>
      <a href="#summary" class="btn-more-on-me">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M5 12l7 7 7-7"/></svg>
        More on Me
      </a>
    </div>
  </div>
</section>'''
    content = content[:old.start()] + replacement + content[old.end():]

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
