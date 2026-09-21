create table if not exists products (
    id integer primary key,
    name text not null,
    platform text not null,
    store text,
    url text not null unique,
    is_active integer not null default 1
);

create table if not exists price_history (
    id integer primary key,
    product_id integer not null references products(id),
    price integer,
    in_stock integer not null default 1,
    checked_at text not null default current_timestamp
);