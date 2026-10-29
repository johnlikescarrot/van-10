import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";
import { NodeCompiler } from "@myriaddreamin/typst-ts-node-compiler";

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scriptDirectory, "..");
const sourceDirectory = path.join(root, "src");
const outputFile = path.join(
  root,
  "DE_CUONG_ON_TAP_GIUA_KI_1_NGU_VAN_10_KNTT_2026_2027.pdf",
);

const compiler = NodeCompiler.create({
  workspace: sourceDirectory,
  fontArgs: [{ fontPaths: [path.join(sourceDirectory, "fonts")] }],
});

const result = compiler.compile({
  mainFilePath: path.join(sourceDirectory, "main.typ"),
});

if (result.hasError()) {
  const diagnostics = result.takeDiagnostics()?.shortDiagnostics ?? [];
  console.error("Typst compilation failed:");
  console.error(JSON.stringify(diagnostics, null, 2));
  process.exit(1);
}

const warnings = result.takeWarnings()?.shortDiagnostics ?? [];
if (warnings.length > 0) {
  console.error("Typst compilation emitted warnings; treat them as build failures:");
  console.error(JSON.stringify(warnings, null, 2));
  process.exit(1);
}

const document = result.result;
const pdf = compiler.pdf(document);
if (!pdf || pdf.length < 1024 || String.fromCharCode(...pdf.slice(0, 4)) !== "%PDF") {
  throw new Error("Compiler did not return a valid PDF payload.");
}

fs.writeFileSync(outputFile, pdf);
console.log(`Built ${path.basename(outputFile)} (${document.numOfPages} pages, ${pdf.length} bytes).`);
