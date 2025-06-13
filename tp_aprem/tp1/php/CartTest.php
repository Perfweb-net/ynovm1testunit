<?php

use PHPUnit\Framework\TestCase;

class CartTest extends TestCase {
    private $cart;

    protected function setUp(): void {
        $this->cart = new Cart();
    }

    public function testAddItem() {
        $item = ['name' => 'Test Item', 'price' => 10, 'quantity' => 2];
        $this->cart->addItem($item);
        
        $items = $this->cart->getItems();
        $this->assertCount(1, $items);
        $this->assertEquals($item, $items[0]);
    }

    public function testGetTotal() {
        $this->cart->addItem(['name' => 'Item 1', 'price' => 10, 'quantity' => 2]);
        $this->cart->addItem(['name' => 'Item 2', 'price' => 15, 'quantity' => 1]);
        
        $this->assertEquals(35, $this->cart->getTotal());
    }

    public function testApplyDiscount() {
        $this->cart->addItem(['name' => 'Item 1', 'price' => 100, 'quantity' => 1]);
        $this->cart->applyDiscount(20);
        
        $this->assertEquals(80, $this->cart->getFinalPrice());
    }

    public function testInvalidDiscount() {
        $this->expectException(InvalidArgumentException::class);
        $this->cart->applyDiscount(150);
    }
} 