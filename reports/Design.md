## Design of The project Big-data Platform

###  Part 1 - Batch data ingestion and transformation (weighted factor for grades = 3)
 The ingestion and transformation will be applied to les of data. Design a schema for a set of
 constraints for data files that mysimbdp will support the ingestion and transformation. Design a
 schema for a set of constraints for tenant service agreement. Explain why you, as a platform provider,
 decide and use such constraints. Implement these constraints into simple con guration les. Provide
 two different examples (e.g., JSON or YAML) for two different tenants to specify constraints on
 service agreement and files for the tenant and explain why such constraints are suitable for the
 tenants. (1 point)

 Two schema for data file constraints

```json
{
    "file_constraints": {
        "allowed_formats": ["csv", "json"],
        "max_file_size_mb": 500,
        "schema": {
            "marketplace": {"type": "string", "required": true, "max_length": 5},
            "customer_id": {"type": "integer", "required": true},
            "review_id": {"type": "string", "required": false},
            "product_id": {"type": "string", "required": true},
            "product_parent": {"type": "integer", "required": true},
            "product_title": {"type": "string", "max_length": 255},
            "product_category": {"type": "string", "required": true},
            "star_rating": {"type": "integer", "min": 1, "max": 5, "required": true},
            "helpful_votes": {"type": "integer", "min": 0},
            "total_votes": {"type": "integer", "min": 0},
            "vine": {"type": "boolean", "required": true},
            "verified_purchase": {"type": "boolean", "required": true},
            "review_headline": {"type": "string", "max_length": 255},
            "review_body": {"type": "string", "max_length": 5000},
            "review_date": {"type": "date", "format": "YYYY-MM-DD", "required": true}
        },
        "encoding": "utf-8",
        "compression": ["gzip", "bzip2"],
        "checksum_validation": true
    }
}

```

For the yaml data constraints:

```yaml
file_constraints:
  allowed_formats: ["csv", "json"]
  max_file_size_mb: 500
  schema:
    marketplace:
      type: string
      required: true
      max_length: 5
    customer_id:
      type: integer
      required: true
    review_id:
      type: string
      required: true
    product_id:
      type: string
      required: true
    product_parent:
      type: integer
      required: true
    product_title:
      type: string
      max_length: 255
    product_category:
      type: string
      required: true
    star_rating:
      type: integer
      min: 1
      max: 5
      required: true
    helpful_votes:
      type: integer
      min: 0
    total_votes:
      type: integer
      min: 0
    vine:
      type: boolean
      required: true
    verified_purchase:
      type: boolean
      required: true
    review_headline:
      type: string
      max_length: 255
    review_body:
      type: string
      max_length: 5000
    review_date:
      type: date
      format: "YYYY-MM-DD"
      required: true
  encoding: "utf-8"
  compression: ["gzip", "bzip2"]
  checksum_validation: true
```

The reason why I need to define some of the item to be ```true``` for the ```required``` field because these data is very important for further identify the customers/poduct/user of the tenants, and it will faciliate further in the tracking.