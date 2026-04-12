(function () {
  const input = document.getElementById('demoInput');
  const btn = document.getElementById('analyzeBtn');
  const output = document.getElementById('demoOutput');

  if (!input || !btn || !output) return;

  const getField = (key) => output.querySelector(`[data-field="${key}"]`);

  function firstSentence(text) {
    return text.split(/[。.!?\n]/).map((s) => s.trim()).filter(Boolean)[0] || text.trim();
  }

  function extractEvidence(text) {
    const words = text.match(/[A-Za-z0-9._-]+/g) || [];
    const hints = words.filter((w) => /(log|report|doc|policy|note|evidence|record|ticket)/i.test(w));
    return hints.slice(0, 3).join(', ') || 'source-text-snippet';
  }

  function extractResponsibility(text) {
    const match = text.match(/(owner|lead|manager|operator|maintainer|負責人|主管|經理|組長)[:：\s]*([\w\u4e00-\u9fa5\- ]{2,40})?/i);
    if (!match) return 'user-owner';
    return (match[2] || match[1] || 'user-owner').trim();
  }

  function suggestSCBKR(text) {
    const normalized = text.trim();
    if (!normalized) {
      return { S: '-', C: '-', B: '-', K: '-', R: '-' };
    }

    const sentence = firstSentence(normalized);
    const S = sentence.slice(0, 80);

    let C = 'Context extracted from input text';
    if (/(because|due to|caused by|因為|導致|由於)/i.test(normalized)) {
      C = 'Cause signal detected (because / due to / 因為 / 導致)';
    }

    let B = 'No explicit boundary found; define operational and policy limits';
    if (/(must|cannot|should not|不得|必須|限制|禁止)/i.test(normalized)) {
      B = 'Boundary signal detected (must / cannot / 必須 / 不得)';
    }

    const K = extractEvidence(normalized);
    const R = extractResponsibility(normalized);

    return { S, C, B, K, R };
  }

  btn.addEventListener('click', function () {
    const result = suggestSCBKR(input.value);
    getField('S').textContent = result.S;
    getField('C').textContent = result.C;
    getField('B').textContent = result.B;
    getField('K').textContent = result.K;
    getField('R').textContent = result.R;
  });
})();
