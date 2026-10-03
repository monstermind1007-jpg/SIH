"""
Root entrypoint proxy forwarding to backend.api_sih:app.
Maintains backward compatibility with uvicorn api:app.
"""
import os
import sys
from dotenv import load_dotenv

_ROOT = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(_ROOT, ".env"))
_BACKEND = os.path.join(_ROOT, "backend")
for _p in [_ROOT, _BACKEND]:
    if _p not in sys.path:
        sys.path.insert(0, _p)

from backend.api_sih import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
