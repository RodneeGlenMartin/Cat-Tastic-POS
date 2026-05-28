package com.example.cattasticpos.domain.model

data class InventoryItem(
    val id: String,
    val itemName: String,
    val unit: String,
    val currentStock: Int,
    val reorderThreshold: Int
)
