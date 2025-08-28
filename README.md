# 🎓 Jifunze - High-Performance E-Learning Platform

[![Django](https://img.shields.io/badge/Django-4.2.16-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8.10-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-orange.svg)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16.2-blue.svg)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7.2.4-red.svg)](https://redis.io/)
[![WebSocket](https://img.shields.io/badge/WebSocket-Real--time-green.svg)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
[![REST API](https://img.shields.io/badge/REST-API-orange.svg)](https://restfulapi.net/)

## 🚀 Overview

**EduPlatform-Django** is a high-performance, scalable e-learning platform built with modern backend technologies. This project demonstrates advanced backend development practices, real-time communication, and AI-ready architecture designed to handle thousands of concurrent users with optimal performance.

## 🎯 Key Features & Technical Highlights

### 🔥 High-Performance Architecture
- **Asynchronous WebSocket Communication**: Real-time chat and notifications using Django Channels
- **Redis Caching Layer**: 15-minute cache middleware for improved response times
- **Database Optimization**: PostgreSQL with connection pooling and query optimization
- **Load Balancing**: Nginx reverse proxy with SSL termination
- **Containerized Deployment**: Docker Compose for scalable microservices architecture

### 🧠 AI-Ready Infrastructure
- **RESTful API Design**: Clean, scalable API endpoints for AI integration
- **Real-time Data Processing**: WebSocket connections for live AI interactions
- **Modular Content System**: Flexible content types supporting AI-generated materials
- **Scalable Database Schema**: Optimized for AI-powered analytics and recommendations

### 📚 Core Functionalities

#### Course Management System
- **Multi-format Content Support**: Text, Video, Image, and File uploads
- **Dynamic Module Ordering**: Custom OrderField for flexible content organization
- **Subject-based Categorization**: Efficient course discovery and filtering
- **Enrollment Management**: Secure student registration and course access

#### Real-time Communication
- **WebSocket Chat System**: Course-specific chat rooms with persistent messaging
- **Live Notifications**: Real-time updates for course activities
- **Scalable Channel Layers**: Redis-backed WebSocket infrastructure

#### User Management & Security
- **Authentication System**: Django's robust user authentication
- **Permission-based Access**: Course enrollment validation
- **SSL/TLS Security**: Production-ready HTTPS implementation
- **CSRF Protection**: Comprehensive security middleware

#### API Architecture
- **RESTful Endpoints**: Clean, documented API for frontend and mobile apps
- **Pagination Support**: Efficient data loading for large datasets
- **Authentication**: Basic auth and token-based security
- **Content Serialization**: Optimized data transfer with DRF serializers

## 🏗️ Technical Architecture

### Backend Stack
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Nginx (SSL)   │    │   Daphne (WS)   │    │   uWSGI (WSGI)  │
│   Load Balancer │    │  WebSocket ASGI │    │  Django App     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   Redis Cache   │
                    │  & Channels     │
                    └─────────────────┘
                                 │
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │   Database      │
                    └─────────────────┘
```

### Performance Optimizations

#### 1. **Caching Strategy**
- Redis-based caching with 15-minute TTL
- Database query result caching
- Static file caching via Nginx
- Session storage optimization

#### 2. **Database Performance**
- PostgreSQL connection pooling
- Optimized queries with `select_related` and `prefetch_related`
- Custom database indexes for frequent queries
- Efficient many-to-many relationship handling

#### 3. **Real-time Communication**
- Asynchronous WebSocket consumers
- Redis channel layer for horizontal scaling
- Efficient message persistence
- Connection pooling for WebSocket clients

#### 4. **API Performance**
- Pagination for large datasets
- Optimized serializers with nested data
- Efficient content type handling
- Rate limiting and authentication caching

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Python 3.8+
- PostgreSQL 16.2
- Redis 7.2.4

### Quick Start
```bash
# Clone the repository
git clone https://github.com/vuthienbao345/EduPlatform-Django.git
cd EduPlatform-Django

# Start the application
docker-compose up -d

# Access the application
# Web Interface: https://localhost
# API Documentation: https://localhost/api/
```

### Development Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## 📊 Performance Metrics

### Scalability Features
- **Horizontal Scaling**: Containerized services for easy scaling
- **Load Balancing**: Nginx reverse proxy with multiple upstream servers
- **Database Scaling**: PostgreSQL with read replicas support
- **Cache Distribution**: Redis cluster support for high availability

### Expected Performance
- **Concurrent Users**: 1000+ simultaneous connections
- **Response Time**: <200ms for cached content
- **WebSocket Connections**: 500+ concurrent real-time connections
- **Database Queries**: Optimized for sub-100ms response times

## 🔧 Configuration

### Environment Variables
```bash
# Database Configuration
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# Django Settings
DJANGO_SETTINGS_MODULE=settings.prod
SECRET_KEY=your-secret-key

# Redis Configuration
REDIS_URL=redis://cache:6379
```

### Production Deployment
```bash
# Build and deploy
docker-compose -f docker-compose.yml up -d --build

# Monitor logs
docker-compose logs -f web

# Scale services
docker-compose up -d --scale web=3
```

## 🧪 API Endpoints

### Course Management
```
GET    /api/subjects/           # List all subjects
GET    /api/subjects/{id}/      # Get subject details
GET    /api/courses/            # List all courses
GET    /api/courses/{id}/       # Get course details
POST   /api/courses/{id}/enroll/ # Enroll in course
GET    /api/courses/{id}/contents/ # Get course contents
```

### WebSocket Endpoints
```
WS     /ws/chat/{course_id}/    # Real-time course chat
```

## 🔒 Security Features

- **SSL/TLS Encryption**: Full HTTPS implementation
- **CSRF Protection**: Cross-site request forgery prevention
- **SQL Injection Prevention**: Django ORM protection
- **XSS Protection**: Content Security Policy headers
- **Authentication**: Secure user session management
- **Permission System**: Role-based access control

## 🎯 AI Integration Ready

The platform is designed with AI integration in mind:

### AI-Ready Features
- **Real-time Data Streaming**: WebSocket connections for AI model inputs
- **Flexible Content API**: Easy integration with AI content generation
- **Scalable Architecture**: Can handle AI model inference workloads
- **Analytics Ready**: Database schema optimized for AI analytics
- **Modular Design**: Easy to add AI-powered features

### Potential AI Enhancements
- **Content Recommendation Engine**: ML-based course suggestions
- **Automated Assessment**: AI-powered quiz generation and grading
- **Natural Language Processing**: Chatbot for student support
- **Content Analysis**: AI-driven content quality assessment
- **Predictive Analytics**: Student performance prediction

## 📈 Monitoring & Debugging

### Built-in Tools
- **Django Debug Toolbar**: Development performance monitoring
- **Redis Board**: Cache monitoring and management
- **uWSGI Stats**: Application server monitoring
- **Nginx Access Logs**: Request monitoring and analytics

### Performance Monitoring
```bash
# Monitor Redis cache
docker-compose exec cache redis-cli monitor

# Check uWSGI stats
curl http://localhost:8000/uwsgi-stats

# Monitor database connections
docker-compose exec db psql -U postgres -c "SELECT * FROM pg_stat_activity;"
```

## 🙏 Acknowledgments

- Django Channels for real-time functionality
- Redis for high-performance caching
- PostgreSQL for robust data storage
- Docker for containerized deployment
- Nginx for load balancing and SSL termination

---

**Built with ❤️ for scalable, high-performance e-learning solutions**
