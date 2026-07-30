const trainCM = [
  [12419, 8, 130, 118, 30, 83, 206],
  [113, 452, 46, 17, 25, 35, 169],
  [304, 21, 1096, 79, 63, 236, 286],
  [561, 0, 13, 5760, 3, 11, 2151],
  [115, 11, 55, 49, 1631, 114, 248],
  [361, 10, 104, 19, 70, 2346, 177],
  [552, 43, 81, 2060, 126, 139, 9398],
];

const testCM = [
  [3170, 7, 46, 40, 7, 27, 52],
  [23, 101, 18, 0, 12, 15, 51],
  [68, 3, 258, 14, 17, 68, 74],
  [151, 0, 3, 1413, 4, 4, 577],
  [35, 6, 19, 14, 372, 33, 75],
  [114, 6, 20, 6, 28, 536, 44],
  [150, 7, 30, 555, 36, 35, 2192],
];

function renderCM(id, matrix) {
  const table = document.getElementById(id);
  const n = matrix.length;
  const rowMax = matrix.map((row) => Math.max(...row));

  let html =
    '<thead><tr><th class="corner"></th>' +
    `<th colspan="${n}" class="axis-label">Predicted</th></tr>`;
  html += '<tr><th class="corner"></th>';
  for (let j = 0; j < n; j++) html += `<th class="axis-label">${j}</th>`;
  html += "</tr></thead><tbody>";

  for (let i = 0; i < n; i++) {
    html += `<tr><th>${i === 0 ? '<span class="axis-label">Actual</span> ' : ""}${i}</th>`;
    for (let j = 0; j < n; j++) {
      const v = matrix[i][j];
      const alpha = rowMax[i] ? v / rowMax[i] : 0;
      html += `<td style="background: rgba(63,63,70,${(alpha * 0.85).toFixed(3)}); color: ${alpha > 0.5 ? "#fff" : "var(--ink)"};">${v.toLocaleString()}</td>`;
    }
    html += "</tr>";
  }
  html += "</tbody>";
  table.innerHTML = html;
}

renderCM("cm-train", trainCM);
renderCM("cm-test", testCM);

