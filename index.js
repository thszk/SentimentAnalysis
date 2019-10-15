const express = require("express")
const expressLayouts = require("express-ejs-layouts")
const bodyparser = require("body-parser")
const { exec } = require("child_process")
const path = require("path")

const app = express()
app.use(bodyparser.json());
const port = process.env.PORT || 3333

app.set("view engine", "ejs")
app.use(expressLayouts)


app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`)
})


app.get("/", (req, res) => {
  res.render("pages/index", {
    output: "",
    input: ""
  })
})

app.get("/freeText/:input", (req, res) => {
  exec(`echo "${req.params.input}" | ${path.resolve("./src/main.py")}`, (error, stdout) => {
    let out
    error ? out = error : out = stdout.split()

    res.render("pages/index", {
      output: out,
      input : req.params.input
    })
  })
})