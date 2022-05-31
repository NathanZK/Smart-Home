from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='172.20.10.5', port=5000, debug=True)
   # app.run(debug=True)
