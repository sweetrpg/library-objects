//
// Tag.swift
// Copyright (c) 2021 Paul Schifferer.
//

import Fluent
import Vapor


public final class Tag : Model {
    public static let schema = Tag.v20210828.schemaName

    @ID
    public var id : UUID?

    @Timestamp(key: Tag.v20210828.createdAt, on: .create)
    public var createdAt : Date?

    @Timestamp(key: Tag.v20210828.updatedAt, on: .update)
    public var updatedAt : Date?

    @Field(key: Tag.v20210828.name)
    public var name : String

    @Timestamp(key: Tag.v20210828.deletedAt, on: .delete)
    public var deletedAt : Date?

    public init() {
    }

    public init(id : UUID? = nil, name : String) {
        self.id = id
        self.name = name
    }

}

extension Tag : Content {}
