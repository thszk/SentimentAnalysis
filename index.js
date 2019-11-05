// libs
const express = require("express")
const expressLayouts = require("express-ejs-layouts")
const bodyparser = require("body-parser")
const { exec } = require("child_process")
const path = require("path")

// preparing to create server
const app = express()
const port = process.env.PORT || 3333
app.use(bodyparser.json())
app.set("view engine", "ejs")
app.use(expressLayouts)

// creating server
app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`)
})

// routes
app.get("/", (req, res) => {
  res.render("pages/home", {
    output: "",
    input: ""
  })
})

app.get("/freeText", (req, res) => {
  res.render("pages/freeText", {
    output: "",
    input: ""
  })
})

app.get("/freeText/:input", (req, res) => {
  let input = JSON.stringify(req.params.input.replace(/%0D%0A/g,"\n")).replace(/\"/g,"")
  
  exec(`echo "${input}" | ${path.resolve("./src/simple-analysis.py")}`, (error, stdout) => {
    let output
    error ? output = error : output = stdout
    res.render("pages/freeText", {
      output,
      input
    })
  })
})

app.get("/airlineAnalysis", (req, res) => {
  res.render("pages/airlineAnalysis", {
    output: "",
    input: ""
  })
})

app.get("/airlineAnalysis/:input", (req, res) => {
  let input = JSON.stringify(req.params.input.replace(/%0D%0A/g,"\n")).replace(/\"/g,"")
  
  exec(`echo "${input}" | python3 ${path.resolve("./src/airline-analysis.py")}`, (error, stdout) => {
    let output
    error ? output = error : output = stdout
    res.render("pages/airlineAnalysis", {
      output,
      input
    })
  })
})