import re

file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

# Hapus seluruh script block yang berisi setLanguage (script lama)
content = re.sub(
    r'<script>\s*// Loading animation.*?// Add transition to nav.*?nav\.style\.transition.*?;\s*</script>',
    '',
    content,
    flags=re.DOTALL
)

# Hapus script block lama yang berisi const translations
content = re.sub(
    r'<script>\s*const translations\s*=.*?</script>',
    '',
    content,
    flags=re.DOTALL
)

# Pastikan hanya ada satu script setLang yang bersih
# Hapus semua script setLang yang ada
content = re.sub(
    r'\n<script>\s*function setLang.*?</script>',
    '',
    content,
    flags=re.DOTALL
)

# Tambah satu script bersih sebelum </body>
clean_script = """
<script>
  /* ── Language Switch ── */
  function setLang(lang) {
    document.querySelectorAll('[data-en]').forEach(function(el) {
      var val = el.getAttribute('data-' + lang);
      if (val !== null) el.innerHTML = val;
    });
    var btnEn = document.getElementById('btn-en');
    var btnId = document.getElementById('btn-id');
    if (btnEn) btnEn.classList.toggle('active', lang === 'en');
    if (btnId) btnId.classList.toggle('active', lang === 'id');
    document.documentElement.lang = lang === 'id' ? 'id' : 'en';
    localStorage.setItem('lang', lang);
  }

  /* ── PDF Certificates ── */
  pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
  document.querySelectorAll('canvas[data-pdf]').forEach(function(canvas) {
    var pdfUrl = canvas.getAttribute('data-pdf');
    var loading = canvas.previousElementSibling;
    pdfjsLib.getDocument(pdfUrl).promise.then(function(pdf) {
      return pdf.getPage(1);
    }).then(function(page) {
      var vp = page.getViewport({ scale: 1 });
      var scale = canvas.parentElement.offsetWidth / vp.width || 1.5;
      var viewport = page.getViewport({ scale: scale });
      canvas.width = viewport.width;
      canvas.height = viewport.height;
      page.render({ canvasContext: canvas.getContext('2d'), viewport: viewport }).promise.then(function() {
        if (loading) loading.style.display = 'none';
      });
    }).catch(function() {
      if (loading) loading.innerHTML = '<svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Preview N/A</span>';
    });
  });

  function openCert(url, title) {
    document.getElementById('certModalTitle').textContent = title;
    document.getElementById('certModalFrame').src = url;
    document.getElementById('certModal').classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeCert() {
    document.getElementById('certModal').classList.remove('open');
    document.getElementById('certModalFrame').src = '';
    document.body.style.overflow = '';
  }
  function closeCertOnBg(e) {
    if (e.target === document.getElementById('certModal')) closeCert();
  }
  document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeCert(); });

  /* ── Init on load ── */
  window.addEventListener('DOMContentLoaded', function() {
    var saved = localStorage.getItem('lang') || 'en';
    setLang(saved);

    /* Scroll progress */
    window.addEventListener('scroll', function() {
      var sp = document.getElementById('scrollProgress');
      if (sp) {
        var pct = (window.pageYOffset / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
        sp.style.width = pct + '%';
      }
    });

    /* Loading overlay */
    setTimeout(function() {
      var lo = document.getElementById('loadingOverlay');
      if (lo) lo.classList.add('hidden');
    }, 600);

    /* Scroll-reveal cards */
    var obs = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) {
        if (e.isIntersecting) { e.target.style.opacity='1'; e.target.style.transform='translateY(0)'; }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll('.exp-card,.project-card,.cert-card,.edu-card').forEach(function(el) {
      el.style.opacity='0'; el.style.transform='translateY(20px)';
      el.style.transition='opacity 0.6s ease, transform 0.6s ease';
      obs.observe(el);
    });
  });
</script>
"""

content = content.replace('</body>', clean_script + '\n</body>', 1)

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
