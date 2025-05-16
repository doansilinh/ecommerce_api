``` bash
ecommerce_api/
│
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── users.py
│   │   │   │   ├── products.py
│   │   │   │   ├── orders.py
│   │   │   │   ├── payments.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── config.py                # config (env vars, DB URL,...)
│   │   ├── security.py              # JWT, OAuth,...
│   │   └── __init__.py
│   ├── crud/
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   └── __init__.py
│   ├── database/
│   │   ├── base.py                  # model Base (SQLAlchemy)
│   │   ├── session.py               # tạo session DB
│   │   └── __init__.py
│   ├── models/
│   │   ├── user.py                  # model bảng user
│   │   ├── product.py               # model bảng product
│   │   ├── order.py                 # model bảng order
│   │   ├── payment.py               # model bảng payment
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── user.py                  # schema user input/output
│   │   ├── product.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │   ├── order_service.py
│   │   ├── payment_service.py
│   │   └── __init__.py
│   ├── main.py                     # app FastAPI entrypoint
│   └── __init__.pp
├── .env
├── requirements.txt
└── README.md
```