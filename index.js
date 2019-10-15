const express = require("express")
const expressLayouts = require("express-ejs-layouts")
const bodyparser = require("body-parser")
const { exec } = require("child_process")
const path = require("path")

const app = express()
app.use(bodyparser.json() );     
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
  let input = JSON.stringify(req.params.input.replace(/%0D%0A/g,"\n")).replace(/\"/g,"")
  
  exec(`echo "${input}" | ${path.resolve("./src/main.py")}`, (error, stdout) => {
    let output
    error ? output = error : output = stdout.split()
    res.render("pages/index", {
      output,
      input
    })
  })
})