import React from 'react';
import Card from 'react-bootstrap/Card';
import { Product } from '../types/product';

interface ProductListProps {
  products: Product[];
  onSelect: (product: Product) => void;
}

const ProductList: React.FC<ProductListProps> = ({ products, onSelect }) => {
  return (
    <div
      style={{
        display: 'flex',
        flexWrap: 'wrap',
        gap: '1.5rem',
        padding: '1.5rem',
      }}
    >
      {products.map((product) => (
        <div
          key={product.id}
          style={{
            flex: '1 1 calc(33.333% - 1.5rem)',
            maxWidth: 'calc(33.333% - 1.5rem)',
            boxSizing: 'border-box',
            margin: '0',
          }}
        >
          <Card
            onClick={() => onSelect(product)}
            style={{
              cursor: 'pointer',
              height: '100%',
              boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
              borderRadius: '8px',
              overflow: 'hidden',
            }}
          >
            <Card.Img
              variant="top"
              src={product.image}
              alt={product.name}
              style={{
                height: '200px',
                objectFit: 'cover',
              }}
            />
            <Card.Body>
              <Card.Title style={{ fontSize: '1.25rem' }}>{product.name}</Card.Title>
              <Card.Text style={{ fontSize: '1.1rem', fontWeight: '500' }}>
                ${product.price.toFixed(2)}
              </Card.Text>
            </Card.Body>
          </Card>
        </div>
      ))}
    </div>
  );
};

export default ProductList;
