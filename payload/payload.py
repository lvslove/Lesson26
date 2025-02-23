valid_create_payload = {
    "name": "Apple MacBook Pro 14 M2",
    "data": {
        "year": 2023,
        "price": 1999.99,
        "CPU model": 'Apple M2 Pro',
        "Hard disk size": "1 TB"
    }
}

invalid_create_payload = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 'dsdsds',
        "price": 1849.99,
        "CPU model": 'Intel Core i9',
        "Hard disk size": "1 TB"
    }
}

update_payload = {
    "name": "Apple MacBook Pro 14 M4",
    "data": {
        "year": 2024,
        "price": 1999.99,
        "CPU model": 'Apple M4 Pro',
        "Hard disk size": "1 TB"
    }
}
