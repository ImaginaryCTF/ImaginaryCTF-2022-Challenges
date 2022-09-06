from flask import Flask, render_template_string, request, Response
import html

app = Flask(__name__)

blacklist = ["{{", "}}", "[", "]", "_"]

@app.route('/', methods=['GET'])
def home():
  print(request.args)
  if "txt" in request.args.keys():
    txt = html.escape(request.args["txt"])
    if any([n in txt for n in blacklist]):
      return "Not allowed."
    if len(txt) <= 69:
      return render_template_string(txt)
    else:
      return "Too long."
  return Response(open(__file__).read(), mimetype='text/plain')

app.run('0.0.0.0', 1337)
