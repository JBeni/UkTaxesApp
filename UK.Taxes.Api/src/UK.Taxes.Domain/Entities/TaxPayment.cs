// <copyright file="TaxPayment.cs" company="Beniamin Jitca">
// Copyright (c) PlaceholderCompany. All rights reserved.
// </copyright>

namespace UK.Taxes.Domain.Entities
{
    using MongoDB.Bson;

    public class TaxPayment
    {
        public ObjectId Id { get; set; }
        public string UserId { get; set; }
        public decimal Amount { get; set; }
        public DateTime PaymentDate { get; set; }
    }
}
