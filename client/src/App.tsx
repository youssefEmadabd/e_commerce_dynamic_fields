import React, { useEffect, useState } from 'react';
import ProductCard from './components/product';
import ProductList from './components/productsList';
import { fetchProductList } from './api/productService';
import { Product } from './types/product';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';

const App: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);
  const [error, setError] = useState<string>('');

  useEffect(() => {
    const loadProducts = async () => {
      try {
        const productList = await fetchProductList();
        setProducts(productList);
      } catch (error) {
        setError('Failed to load products.');
      }
    };

    loadProducts();
  }, []);

  const handleSelectProduct = (product: Product) => {
    setSelectedProduct(product);
  };

  const handleBackToList = () => {
    setSelectedProduct(null);
  };

  return (
    <div style={{ display: 'flex', height: '100vh', width: '100vw', justifyContent: 'center', alignItems: 'center' }}>
      <Container fluid>
        {selectedProduct ? (
          <Row>
            <Col xs={12} style={{ padding: '1rem' }}>
              <Button variant="secondary" onClick={handleBackToList} style={{ marginBottom: '1rem' }}>
                Back to Products
              </Button>
              <ProductCard product={selectedProduct} />
            </Col>
          </Row>
        ) : (
          <Row>
            <Col xs={12} style={{ padding: '1rem' }}>
              <h5 style={{marginLeft: "32px"}}>Product List</h5>
              {error && <p style={{ color: 'red' }}>{error}</p>}
              <ProductList products={products} onSelect={handleSelectProduct} />
            </Col>
          </Row>
        )}
      </Container>
    </div>
  );
};

export default App;
