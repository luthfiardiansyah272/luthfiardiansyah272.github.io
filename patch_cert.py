import re

file = r'd:\FILE LUTHFI\JOB HUNTER\CV New\index.html'
with open(file, 'r', encoding='utf-8') as f:
    content = f.read()

new_cert = '''<!-- CERTIFICATIONS -->
<section id="certifications">
  <div class="container">
    <span class="section-title">Certifications &amp; Training</span>
    <div class="cert-grid">

      <div class="cert-card" onclick="openCert('certificate/1. Sertifikat AK3U_13.pdf','Ahli K3 Umum')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/1. Sertifikat AK3U_13.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge k3">K3</span><div class="cert-title">Ahli K3 Umum</div><div class="cert-issuer">Kemnaker RI &middot; Mutiara Mutu Sertifikasi</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/1. Sertifikat SBC_HIRAC_13.pdf','HIRAC')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/1. Sertifikat SBC_HIRAC_13.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge k3">K3</span><div class="cert-title">HIRAC &ndash; Hazard Identification &amp; Risk Assessment</div><div class="cert-issuer">SBC Training</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/2. Sertifikat SBC_JSA_13.pdf','Job Safety Analysis')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/2. Sertifikat SBC_JSA_13.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge k3">K3</span><div class="cert-title">Job Safety Analysis (JSA)</div><div class="cert-issuer">SBC Training</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/13. Sertifikat SBC_9001_13.pdf','ISO 9001')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/13. Sertifikat SBC_9001_13.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge iso">ISO</span><div class="cert-title">ISO 9001 &ndash; Quality Management System</div><div class="cert-issuer">SBC Training</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/14. Sertifikat SBC_14001_13.pdf','ISO 14001')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/14. Sertifikat SBC_14001_13.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge iso">ISO</span><div class="cert-title">ISO 14001 &ndash; Environmental Management</div><div class="cert-issuer">SBC Training</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/15. Sertifikat SBC_45001_13.pdf','ISO 45001')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/15. Sertifikat SBC_45001_13.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge iso">ISO</span><div class="cert-title">ISO 45001 &ndash; OH&amp;S Management</div><div class="cert-issuer">SBC Training</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/9. Sertifikat SBC_19011_13.pdf','ISO 19011')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/9. Sertifikat SBC_19011_13.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge iso">ISO</span><div class="cert-title">ISO 19011 &ndash; Audit Management Guidelines</div><div class="cert-issuer">SBC Training</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/Luthfi_Ardiansyah_ORBITFA62fba296092c1.pdf','AI Mastery Program')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/Luthfi_Ardiansyah_ORBITFA62fba296092c1.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge ai">AI</span><div class="cert-title">Artificial Intelligence Mastery Program</div><div class="cert-issuer">MSIB Kampus Merdeka</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/LuthfiArdiansyah-FGA Big Data usi-certificate (2).pdf','Big Data FGA')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/LuthfiArdiansyah-FGA Big Data usi-certificate (2).pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge data">Data</span><div class="cert-title">Big Data &ndash; Fresh Graduate Academy</div><div class="cert-issuer">Digitalent Kominfo</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/sertifikat scada.pdf','SCADA Training')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/sertifikat scada.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge scada">SCADA</span><div class="cert-title">SCADA System Training</div><div class="cert-issuer">Industrial Automation</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/Sertifikat Magang PLN.pdf','Internship PT PLN')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/Sertifikat Magang PLN.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge intern">Internship</span><div class="cert-title">Internship Certificate &ndash; PT PLN</div><div class="cert-issuer">PT PLN ULP Tanjung Karang</div></div>
      </div>

      <div class="cert-card" onclick="openCert('certificate/sertif hima.pdf','HIMATRO')">
        <div class="cert-thumb"><div class="cert-loading"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#94a3b8" stroke-width="1.5"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg><span>Loading...</span></div><canvas data-pdf="certificate/sertif hima.pdf"></canvas></div>
        <div class="cert-info"><span class="cert-badge org">Org</span><div class="cert-title">Active Member &ndash; HIMATRO</div><div class="cert-issuer">Universitas Lampung</div></div>
      </div>

    </div>
  </div>
</section>

<!-- CERT MODAL -->
<div class="cert-modal" id="certModal" onclick="closeCertOnBg(event)">
  <div class="cert-modal-inner">
    <div class="cert-modal-header">
      <h3 id="certModalTitle">Certificate</h3>
      <button class="cert-modal-close" onclick="closeCert()">&times;</button>
    </div>
    <div class="cert-modal-body">
      <iframe id="certModalFrame" src=""></iframe>
    </div>
  </div>
</div>'''

content = re.sub(r'<!-- CERTIFICATIONS -->.*?</section>', new_cert, content, flags=re.DOTALL)

# Also inject pdf.js script before </body>
pdfjs_script = '''
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
<script>
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
</script>
'''

if pdfjs_script.strip() not in content:
    content = content.replace('</body>', pdfjs_script + '\n</body>')

with open(file, 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
