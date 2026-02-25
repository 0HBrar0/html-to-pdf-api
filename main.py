from fastapi import FastAPI, Request, Response
from weasyprint import HTML

app = FastAPI()

@app.post("/html-to-pdf")
async def convert_to_pdf(request: Request):
    body = await request.json()
    html_content = body.get("html")
    pdf_bytes = HTML(string=html_content).write_pdf()
    return Response(content=pdf_bytes, media_type="application/pdf")