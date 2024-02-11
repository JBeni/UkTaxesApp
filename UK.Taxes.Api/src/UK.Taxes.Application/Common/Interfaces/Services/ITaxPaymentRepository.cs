using MongoDB.Bson;
using UK.Taxes.Domain.Entities;

namespace UK.Taxes.Application.Common.Interfaces.Services
{
    public interface ITaxPaymentRepository
    {
        Task<TaxPayment> GetByIdAsync(ObjectId id);
        Task<IEnumerable<TaxPayment>> GetByUserIdAsync(string userId);
        Task<IEnumerable<TaxPayment>> GetAllAsync();
        Task CreateAsync(TaxPayment taxPayment);
        Task UpdateAsync(TaxPayment taxPayment);
        Task DeleteAsync(ObjectId id);
    }
}
