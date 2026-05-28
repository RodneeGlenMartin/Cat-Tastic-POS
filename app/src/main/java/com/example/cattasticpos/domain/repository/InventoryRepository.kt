package com.example.cattasticpos.domain.repository

import com.example.cattasticpos.domain.model.InventoryItem
import kotlinx.coroutines.flow.Flow

interface InventoryRepository {
    fun getAllInventory(): Flow<List<InventoryItem>>
    suspend fun insertInventoryItems(items: List<InventoryItem>)
    suspend fun decrementStock(inventoryId: String, amount: Int)
    suspend fun restockItem(itemId: String, addedAmount: Int)
}
