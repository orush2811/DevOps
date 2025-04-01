provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "kubernetes_deployment" "weather_app" {
  metadata {
    name = "weather-app"
    labels = {
      app = "weather-app"
    }
  }
  spec {
    replicas = 2
    selector {
      match_labels = {
        app = "weather-app"
      }
    }
    template {
      metadata {
        labels = {
          app = "weather-app"
        }
      }
      spec {
        container {
          image = "weather-app:latest"
          name  = "weather-app"
          image_pull_policy = "Never"  # Forces use of local image - this is temporary, remove it if needed to deploy via the cloud
          port {
            container_port = 8080
          }
          env {
            name  = "WEATHER_API_KEY"
            value = "API-KEY"
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "weather_app" {
  metadata {
    name = "weather-app-service"
  }
  spec {
    selector = {
      app = "weather-app"
    }
    port {
      port        = 80
      target_port = 8080
    }
    type = "NodePort"
  }
}