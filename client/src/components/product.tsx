import React from 'react';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { Product } from '../types/product';

interface ProductCardProps {
  product: Product;
}

const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  return (
    <Card style={{ width: '18rem', margin: 'auto' }}>
      <Card.Img variant="top" src={product.image } />
      <Card.Body>
        <Card.Title>{product.name}</Card.Title>
        <Card.Text>
          <strong>Brand:</strong> {product.brand_name} <br />
          <strong>Model:</strong> {product.model_number} <br />
          <strong>Type:</strong> {product.type} <br />
          <strong>Description:</strong> {product.description} <br />
          <strong>Price:</strong> ${product.price.toFixed(2)} <br />
          <strong>Quantity:</strong> {product.quantity}
        </Card.Text>
      </Card.Body>
    </Card>
  );
};

export default ProductCard;
