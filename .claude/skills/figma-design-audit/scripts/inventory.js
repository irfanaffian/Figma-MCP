// Read-only inventory for figma-design-audit. Run with use_figma.
// Replace PAGE_ID (the page that holds the frame) and FRAME_ID (the page frame to audit).
// Optional: adjust ALLOWED_TEXT_COLORS to the project's tokens (hex without #).
const PAGE_ID = "11:2160";
const FRAME_ID = "215:90";
const ALLOWED_TEXT_COLORS = new Set(["21211f", "807a73", "ffffff"]);
const ALLOWED_LH = [100, 110, 115, 120, 125, 130, 145, 150];

const pg = await figma.getNodeByIdAsync(PAGE_ID);
await figma.setCurrentPageAsync(pg);
const frame = await figma.getNodeByIdAsync(FRAME_ID);

const vis = n => { let p = n; while (p && p.id !== FRAME_ID) { if (!p.visible) return false; p = p.parent; } return true; };
const hex = c => [c.r, c.g, c.b].map(v => Math.round(v * 255).toString(16).padStart(2, "0")).join("");
const top = n => { let p = n; while (p.parent && p.parent.id !== FRAME_ID) p = p.parent; return p.name.slice(0, 22); };

const texts = frame.findAllWithCriteria({ types: ["TEXT"] }).filter(vis);
const styles = new Map(), textColors = new Map(), families = new Set(), flags = [];
for (const t of texts) {
  for (const s of t.getStyledTextSegments(["fontName", "fontSize", "lineHeight", "letterSpacing", "fills"])) {
    families.add(s.fontName.family);
    const lh = s.lineHeight.unit === "AUTO" ? "auto" : Math.round(s.lineHeight.value) + (s.lineHeight.unit === "PERCENT" ? "%" : "px");
    const key = [s.fontName.family, s.fontName.style, s.fontSize, lh, Math.round(s.letterSpacing.value) + "%"].join(" | ");
    if (!styles.has(key)) styles.set(key, []);
    const ex = styles.get(key); if (ex.length < 2) ex.push(top(t) + ": " + s.characters.slice(0, 16).replace(/\n/g, " "));
    const f = s.fills[0];
    if (f && f.type === "SOLID") {
      const h = hex(f.color); textColors.set(h, (textColors.get(h) || 0) + 1);
      if (!ALLOWED_TEXT_COLORS.has(h)) flags.push("text color " + h + " — " + top(t) + ": " + s.characters.slice(0, 16));
    }
    if (s.fontSize % 2 === 1 && s.fontSize < 60) flags.push("odd size " + s.fontSize + " — " + top(t) + ": " + s.characters.slice(0, 16));
    if (s.lineHeight.unit === "PERCENT" && !ALLOWED_LH.includes(Math.round(s.lineHeight.value))) flags.push("line-height " + Math.round(s.lineHeight.value) + "% — " + top(t));
  }
}

const nonTextColors = new Map();
for (const n of frame.findAll(n => n.type !== "TEXT" && vis(n))) for (const prop of ["fills", "strokes"]) {
  if (!(prop in n) || n[prop] === figma.mixed) continue;
  for (const p of n[prop]) if (p.type === "SOLID" && p.visible !== false) { const h = hex(p.color); nonTextColors.set(h, (nonTextColors.get(h) || 0) + 1); }
}

const overflow = [];
for (const t of texts) { const p = t.parent; if (!p || !("clipsContent" in p)) continue;
  if ((t.y + t.height > p.height + 0.5 || t.x + t.width > p.width + 0.5) && (p.layoutMode === "NONE" || p.clipsContent)) overflow.push(top(t) + ": " + t.characters.slice(0, 20)); }

const badIcons = [];
for (const v of frame.findAllWithCriteria({ types: ["VECTOR"] }).filter(vis))
  if (v.strokes.length && v.parent && /Phosphor/.test(v.parent.name)) { const want = v.parent.width * 16 / 256; if (Math.abs(v.strokeWeight - want) > 0.05) badIcons.push(top(v) + " / " + v.parent.name + " " + v.strokeWeight + " ≠ " + want.toFixed(2)); }

const buttons = {};
for (const f of frame.findAllWithCriteria({ types: ["FRAME"] }).filter(vis).filter(f => f.findChild && f.findChild(c => c.name === "Trailing icon container"))) {
  const l = f.findOne(n => n.type === "TEXT");
  const k = [Math.round(f.height) + "h", "r" + f.cornerRadius, "gap" + f.itemSpacing, "pad" + [f.paddingTop, f.paddingRight, f.paddingBottom, f.paddingLeft].join("/"), f.fills[0] && f.fills[0].color ? hex(f.fills[0].color) : "-", l ? l.fontName.family + " " + l.fontSize : ""].join(" · ");
  buttons[k] = (buttons[k] || 0) + 1;
}

const sections = frame.children.filter(c => c.visible && c.height > 40 && !/^Vector|Grid marker|Icon$/.test(c.name)).sort((a, b) => a.y - b.y);
const joins = [];
for (let i = 1; i < sections.length; i++) { const g = Math.round(sections[i].y - (sections[i - 1].y + sections[i - 1].height)); if (g !== 0) joins.push(sections[i - 1].name.slice(0, 20) + " → " + sections[i].name.slice(0, 20) + ": " + g + "px"); }
const offGrid = sections.filter(c => Math.round(c.height) % 4 !== 0).map(c => c.name.slice(0, 24) + " " + Math.round(c.height));

return {
  textStyleCount: styles.size, families: [...families],
  textColors: Object.fromEntries(textColors),
  nonTextColors: Object.fromEntries([...nonTextColors].sort((a, b) => b[1] - a[1])),
  flags, overflow, badIcons, buttons, sectionJoins: joins, offGridHeights: offGrid,
  styles: [...styles.entries()].map(([k, v]) => k + "  ← " + v.join(" ; ")),
};
