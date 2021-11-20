from flask import Flask, request

app = Flask(__name__)


@app.route("/deploy", methods=["GET", "POST"])
def hello_world():
    requestData = request.get_json()
    company_name = requestData["company_name"]
    web_url = f"https://{ company_name }.subscriby.shop"
    return web_url


@app.route("/", methods=["GET"])
def home_page():

    return """<!DOCTYPE html>
<head>
</head>
<body>
<h1>New shop by Joel enterprises</h1>
<form id="new_shop" action=/deploy method="post">
   <label> Name </label> 
   <input name="name" required>
   <label> Company Name </label>
   <input id="company_name"  required>
   <button type="submit"> submit </button>
</form>
</body>
<script>
document.querySelector("#new_shop").addEventListener("submit", function(event){
event.preventDefault();
async function postData(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST', 
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
};

companyName = {company_name: document.querySelector("#company_name").value}
console.log(companyName);
postData('http://127.0.0.1:5000/deploy', companyName)
  .then(data => {
    console.log(data); // JSON data parsed by data.json() call
  });
})
</script>
"""
