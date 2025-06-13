<?php

class Cart {
    private $items = [];
    private $discount = 0;

    public function addItem($item) {
        $this->items[] = $item;
    }

    public function getItems() {
        return $this->items;
    }

    public function getTotal() {
        $total = 0;
        foreach ($this->items as $item) {
            $total += $item['price'] * $item['quantity'];
        }
        return $total;
    }

    public function applyDiscount($percentage) {
        if ($percentage < 0 || $percentage > 100) {
            throw new InvalidArgumentException("Le pourcentage de remise doit être entre 0 et 100");
        }
        $this->discount = $percentage;
    }

    public function getFinalPrice() {
        $total = $this->getTotal();
        return $total * (1 - $this->discount / 100);
    }
} 