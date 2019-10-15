const express = require("express")
const expressLayouts = require("express-ejs-layouts")
const { exec } = require("child_process")
const path = require("path")

const app = express()
const port = process.env.PORT || 3333

app.set("view engine", "ejs")
app.use(expressLayouts)


app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`)
})


app.get("/", (req, res) => {
  exec(path.resolve("./src/main.py"), (error, stdout) => {
    let out
    if (error) out = "erro"  
    else out = stdout

    res.render("pages/index", {
      output: out
    })
  })
})

app.get("/dev", (req, res) => {
  res.render("pages/dev")
})