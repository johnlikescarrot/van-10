import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scriptDirectory, "..");
const outputFile = path.join(
  root,
  "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf",
);

if (!fs.existsSync(outputFile)) {
  console.error(`Missing output PDF: ${outputFile}`);
  process.exit(1);
}

const pdf = fs.readFileSync(outputFile);
const header = pdf.subarray(0, 5).toString("ascii");
const trailerPresent = pdf.subarray(Math.max(0, pdf.length - 4096)).includes(
  Buffer.from("%%EOF"),
);

if (header !== "%PDF-" || pdf.length < 100_000 || !trailerPresent) {
  console.error(
    `PDF sanity check failed (header=${JSON.stringify(header)}, bytes=${pdf.length}, eof=${trailerPresent}).`,
  );
  process.exit(1);
}

console.log(`PDF sanity check passed: ${path.basename(outputFile)} (${pdf.length} bytes).`);
