import http.server, os, socket, sys, threading, webbrowser
from pathlib import Path

def main():
    root = (Path(sys._MEIPASS) / 'game') if getattr(sys, 'frozen', False) else (Path(__file__).resolve().parent / 'game')
    os.chdir(root)
    with socket.socket() as s:
        s.bind(('127.0.0.1', 0)); port = s.getsockname()[1]
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args): pass
    server = http.server.ThreadingHTTPServer(('127.0.0.1', port), Quiet)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    url = f'http://127.0.0.1:{port}/index.html'
    print('CHISHTI BRO: PAKISTAN OPEN WORLD — FINAL EDITION')
    print('Game URL:', url); webbrowser.open(url)
    try: threading.Event().wait()
    except KeyboardInterrupt: server.shutdown()
if __name__ == '__main__': main()
