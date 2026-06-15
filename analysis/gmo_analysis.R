library(tidyverse)
library(ggplot2)
library(dplyr)
library(readr)

# Dataseti yüklə
df <- read_csv("C:/Users/SARN/gmo-safety-dashboard/data/gmo_dataset_clean.csv")

# Ümumi baxış
cat("=== Dataset Overview ===\n")
cat("Total GMO products:", nrow(df), "\n")
cat("Crop types:", length(unique(df$crop_type)), "\n")
print(summary(df$risk_score))

# ANOVA - risk score kateqoriyalar arasında fərqlidirmi?
cat("\n=== ANOVA Test ===\n")
anova_result <- aov(risk_score ~ crop_type, data = df)
print(summary(anova_result))

# Boxplot
ggplot(df, aes(x = crop_type, y = risk_score, fill = crop_type)) +
  geom_boxplot() +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  labs(title = "Risk Score Distribution by Crop Type",
       x = "Crop Type", y = "Risk Score") +
  theme(legend.position = "none")