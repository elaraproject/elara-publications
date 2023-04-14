const path = require('path');
const puppeteer = require("puppeteer");
const report = require("puppeteer-report");


async function generatePDF() {
    const browser = await puppeteer.launch({
      args: ["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"],
    });
    try {
      const file = path.join(__dirname, "paper-1.html");
      console.log(`Processing ${file}`);
      await report.pdf(browser, file, {
        path: "paper-1.pdf",
        format: "A4",
      });
    } finally {
      await browser.close();
    }
    console.log("Done!")
}

generatePDF();
