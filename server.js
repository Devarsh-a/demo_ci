const http = require("http");

const PORT = 3000;

const html = `
<!DOCTYPE html>
<html>
<head>
<title>CI Demo</title>
</head>
<body>
<h1 id="title">Jenkins CI Working</h1>
<input id="name" placeholder="enter name"/>
<button onclick="document.getElementById('title').innerText='Hello ' + document.getElementById('name').value">Submit</button>
</body>
</html>
`;

http.createServer((req,res)=>{
    res.writeHead(200,{"Content-Type":"text/html"});
    res.end(html);
}).listen(PORT,()=>console.log("Server running on "+PORT));