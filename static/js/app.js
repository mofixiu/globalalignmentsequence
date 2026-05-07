document.getElementById('alignForm').addEventListener('submit', async function (e) {
  e.preventDefault();
  const form = e.target;
  const data = {
    seq1: form.seq1.value.trim(),
    seq2: form.seq2.value.trim(),
    match: form.match.value,
    mismatch: form.mismatch.value,
    gap: form.gap.value
  };
  const res = await fetch('/api/align', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  const json = await res.json();
  if (res.ok) {
    document.getElementById('score').textContent = `Score: ${json.score}`;
    document.getElementById('aln1').textContent = json.alignment.a1;
    document.getElementById('aln2').textContent = json.alignment.a2;
  } else {
    document.getElementById('score').textContent = `Error: ${json.error || res.statusText}`;
  }
});

document.getElementById('clear').addEventListener('click', function () {
  const f = document.getElementById('alignForm');
  f.seq1.value = '';
  f.seq2.value = '';
  document.getElementById('score').textContent = '-';
  document.getElementById('aln1').textContent = '-';
  document.getElementById('aln2').textContent = '-';
});
