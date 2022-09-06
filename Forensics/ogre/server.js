const express = require("express");
const fs = require("fs");
const app = express();

app.set("view engine", "ejs");
app.use(express.static("public"));

const quotesRaw = fs.readFileSync("quotes.json");
const quotes = JSON.parse(quotesRaw);

app.get("/", function (req, res) {
  res.render("index", {
    quote: quotes[Math.floor(Math.random() * quotes.length)],
  });
});

app.listen(8080);
console.log("Server is listening on port 8080");
