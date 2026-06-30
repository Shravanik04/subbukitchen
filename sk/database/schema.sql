-- Subbu's Kitchen - Database Schema

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

-- Index for slot checking queries
CREATE INDEX IF NOT EXISTS idx_date_time ON orders(order_date, order_time);
