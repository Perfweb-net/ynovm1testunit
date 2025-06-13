const Cart = require('./Cart');

describe('Cart', () => {
    let cart;

    beforeEach(() => {
        cart = new Cart();
    });

    test('should add item to cart', () => {
        const item = { name: 'Test Item', price: 10, quantity: 2 };
        cart.addItem(item);
        
        const items = cart.getItems();
        expect(items).toHaveLength(1);
        expect(items[0]).toEqual(item);
    });

    test('should calculate total correctly', () => {
        cart.addItem({ name: 'Item 1', price: 10, quantity: 2 });
        cart.addItem({ name: 'Item 2', price: 15, quantity: 1 });
        
        expect(cart.getTotal()).toBe(35);
    });

    test('should apply discount correctly', () => {
        cart.addItem({ name: 'Item 1', price: 100, quantity: 1 });
        cart.applyDiscount(20);
        
        expect(cart.getFinalPrice()).toBe(80);
    });

    test('should throw error for invalid discount', () => {
        expect(() => {
            cart.applyDiscount(150);
        }).toThrow('Le pourcentage de remise doit être entre 0 et 100');
    });
}); 