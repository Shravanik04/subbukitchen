from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
import os
from datetime import datetime, timedelta

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.executescript('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                phone TEXT NOT NULL,
                menu_item TEXT NOT NULL,
                quantity INTEGER NOT NULL DEFAULT 1,
                spice_level TEXT NOT NULL DEFAULT 'medium',
                order_date TEXT NOT NULL,
                order_time TEXT NOT NULL,
                delivery_type TEXT NOT NULL DEFAULT 'delivery',
                address TEXT,
                latitude REAL,
                longitude REAL,
                special_instructions TEXT,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order')
def order():
    item = request.args.get('item', '')
    return render_template('order.html', selected_item=item)

@app.route('/api/place-order', methods=['POST'])
def place_order():
    data = request.get_json()
    
    VALID_ITEMS = ["Subbu's Chapati Box", "Subbu's Normal Meals", "Subbu's Meals"]
    if data.get('menu_item') not in VALID_ITEMS:
        return jsonify({'success': False, 'message': 'Invalid menu item selected'})

    required = ['customer_name', 'phone', 'menu_item', 'order_date', 'order_time']
    for field in required:
        if not data.get(field):
            return jsonify({'success': False, 'message': f'{field} is required'})
    
    with get_db() as conn:
        cursor = conn.execute('''
            INSERT INTO orders 
            (customer_name, phone, menu_item, quantity, spice_level, order_date, order_time,
             delivery_type, address, latitude, longitude, special_instructions)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['customer_name'], data['phone'], data['menu_item'],
            data.get('quantity', 1), data.get('spice_level', 'medium'),
            data['order_date'], data['order_time'],
            data.get('delivery_type', 'delivery'), data.get('address', ''),
            data.get('latitude'), data.get('longitude'),
            data.get('special_instructions', '')
        ))
        order_id = cursor.lastrowid
    
    return jsonify({
        'success': True,
        'order_id': order_id,
        'message': 'Order placed successfully!'
    })

@app.route('/success/<int:order_id>')
def success(order_id):
    with get_db() as conn:
        order = conn.execute("SELECT * FROM orders WHERE id=?", (order_id,)).fetchone()
    if not order:
        return redirect(url_for('index'))
    return render_template('success.html', order=dict(order))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
