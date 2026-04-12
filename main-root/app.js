(function () {
  const btn = document.getElementById('downloadZipBtn');
  const status = document.getElementById('zipStatus');

  if (!btn) return;

  const starterFiles = [
    'starter-package/README.txt',
    'starter-package/DEPLOY_AND_AUTOINDEX.md',
    'starter-package/tools/auto_index.py',
    'starter-package/memory-index/index.scbkr.json',
    'starter-package/memory-index/json/sample-memory.json',
    'starter-package/memory-index/drive-import/.keep',
    'starter-package/memory-index/local-private/.keep'
  ];

  async function fetchTextFile(path) {
    const res = await fetch(path, { cache: 'no-cache' });
    if (!res.ok) {
      throw new Error(`Failed to fetch ${path}: ${res.status}`);
    }
    return res.text();
  }

  async function buildZip() {
    if (!window.JSZip) {
      throw new Error('JSZip not loaded');
    }

    const zip = new window.JSZip();
    for (const filePath of starterFiles) {
      const content = await fetchTextFile(filePath);
      zip.file(filePath.replace('starter-package/', ''), content);
    }

    return zip.generateAsync({ type: 'blob' });
  }

  btn.addEventListener('click', async function () {
    try {
      btn.disabled = true;
      status.textContent = '正在建立 ZIP / Building ZIP...';

      const zipBlob = await buildZip();
      const downloadUrl = URL.createObjectURL(zipBlob);
      const anchor = document.createElement('a');
      anchor.href = downloadUrl;
      anchor.download = 'scbkr-memory-index-starter.zip';
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();
      URL.revokeObjectURL(downloadUrl);

      status.textContent = 'ZIP 已建立並開始下載。ZIP built and download started.';
    } catch (error) {
      console.error(error);
      status.textContent =
        'ZIP 建立失敗，請直接下載 repository ZIP 或檢查網路是否可載入 JSZip。';
    } finally {
      btn.disabled = false;
    }
  });
})();
