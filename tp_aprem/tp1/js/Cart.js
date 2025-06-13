class Cart {
    constructor() {
        this.items = [];
        this.discount = 0;
    }

    addItem(item) {
        this.items.push(item);
    }

    getItems() {
        return this.items;
    }

    getTotal() {
        return this.items.reduce((total, item) => {
            return total + (item.price * item.quantity);
        }, 0);
    }

    applyDiscount(percentage) {
        if (percentage < 0 || percentage > 100) {
            throw new Error("Le pourcentage de remise doit être entre 0 et 100");
        }
        this.discount = percentage;
    }

    getFinalPrice() {
        const total = this.getTotal();
        return total * (1 - this.discount / 100);
    }
}

module.exports = Cart; 