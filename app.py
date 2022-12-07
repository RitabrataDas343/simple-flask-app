from flask import Flask, render_template

app = Flask(  
	__name__,
	template_folder='templates',  
	static_folder='static'  
)

@app.route('/')  
def base_page():
	random_num = 34
	return render_template(
		'base.html',  
		random_number=random_num  
	)


@app.route('/2')
def page_2():
	return render_template('site_2.html', random_str="20CS8002")


if __name__ == "__main__":  
	app.run( 
		host='0.0.0.0',  
		port=8000
	)