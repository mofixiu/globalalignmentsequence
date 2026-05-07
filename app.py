from flask import Flask, request, render_template, jsonify

from cli_align import global_alignment

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/align', methods=['POST'])
def api_align():
    data = request.get_json() or request.form
    seq1 = data.get('seq1', '')
    seq2 = data.get('seq2', '')
    try:
        match = int(data.get('match', 1))
        mismatch = int(data.get('mismatch', -1))
        gap = int(data.get('gap', -1))
    except Exception:
        return jsonify({'error': 'Invalid scoring parameters'}), 400

    score, alignment = global_alignment(seq1, seq2, match, mismatch, gap)
    return jsonify({'score': score, 'alignment': {'a1': alignment[0], 'a2': alignment[1]}})


if __name__ == '__main__':
    app.run(debug=True)
